# -*- coding: utf-8 -*-
from odoo import fields, models
import numpy as np
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    """ sale model"""
    _inherit = 'sale.order'

    project_count = fields.Integer(compute='_compute_project_counts')

    def action_create_projects(self):
        """ action to create project task and subtask"""
        if self.order_line:
            var = self.env['project.project'].create({
                'name': self.name,
            })
            self.write({'project_id': var.id, })
            mile = self.mapped('order_line.milestone')
            milestones = np.unique(mile)
            for new in milestones:
                task = self.env['project.task'].create({
                    'name': 'milestone - ' + str(new),
                    'project_id': var.id,
                    'milestone': new,
                })
                for rec in self.order_line.filtered(lambda x: x.milestone == task.milestone):
                    print(rec)
                    a = self.env['project.task'].create({
                        'name': task.name + rec.product_template_id.name,
                        'parent_id': task.id,
                        'sale_order_line_milestone_id': rec.id,
                        'milestone': new,

                    })

        else:
            raise ValidationError("Please enter product")

    def get_project(self):
        """ smart button to get products"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Projects',
            'view_mode': 'tree,form',
            'res_model': 'project.project',
            'domain': [('id', '=', self.project_id.id)],
            'context': "{'create': False}"
        }

    def _compute_project_counts(self):
        """ to get the project count"""
        for rec in self:
            rec.project_count = self.env['project.project'].search([('id', '=', self.project_id.id)])

    def action_update_project(self):
        """ update project"""
        orderline_tasks = []
        for rec in self.order_line:
            task_name = f'milestone - {rec.milestone}'
            all_tasks = self.project_id.task_ids.mapped('name')
            main_task_id = self.project_id.task_ids.filtered(lambda x: x.name == task_name)
            all_child_tasks = main_task_id.child_ids.mapped('name')
            child_task_name = f'{task_name} {rec.product_id.name}'
            if task_name in all_tasks:
                if child_task_name not in all_child_tasks:
                    self.env['project.task'].create({
                        'name': child_task_name,
                        'parent_id': main_task_id.id
                    })
            else:
                self.env['project.task'].create({
                    'name': child_task_name,
                    'parent_id': self.env['project.task'].create({
                        'name': task_name,
                        'project_id': self.project_id.id
                    }).id
                })
            orderline_tasks.append(task_name)
            orderline_tasks.append(child_task_name)
        updated_tasks = self.project_id.task_ids.mapped('name')
        for elem in set(updated_tasks).difference(orderline_tasks):
            self.project_id.task_ids.filtered(lambda x: x.name == elem).unlink()

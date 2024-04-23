{
    'name': "real estate 2",
    'version': '17.0.1.0.0',
    'depends': ['base'],
    'author': "Author",
    'category': 'category',
    'description': """
   its about the real estate
    """,
    'summary': 'summery',
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menu.xml',

    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #
    #
    # ],
    'application': True,
    'installable': True,

}

#
# //        _onLeaveChange: function (evt) {
# //        console.log("Leave onchange function triggered");
# //        var start_date = new Date($('#start_date').val());
# //        var end_date = new Date($('#end_date').val());
# //                var current_date = start_date;
# //                 var all_days = 0;
# //                if (start_date > end_date) {
# //
# //                    $('#total_days').val(all_days);
# //                   $('#end_date').removeClass('is-valid').addClass('is-invalid');
# ////                   $('#end_date').removeClass('is-invalid').addClass('is-valid');
# //
# //                }
# //                else{
# //                    var total = 0;
# //
# //                    start_date.setHours(0,0,0,0);
# //                    end_date.setHours(0,0,0,0);
# # ////
# //                    var current = new Date(start_date);
# //                    current.setDate(current.getDate() + 1);
# //                    var day;
# //                    while (current <= end_date) {
# //                        day = current.getDay();
# //                        if (day >= 1 && day <= 5) {
# //                            ++total;
# //                        }
# //                        current.setDate(current.getDate() + 1);
# //                    }
# //                    var all_days = total + 1;
# //
# //                     $('#total_days').val(all_days);
# //                                        $('#end_date').removeClass('is-invalid').addClass('is-valid');
# //
# //                    }


# print(contact)
# if rec.answer.name == 'name':
#     contact = request.env['res.partner'].create({
#         'name': arr[0]
#     })
#     user_input.contact_id = contact.id
# user_input.contact_id.write({
#     rec.answer.name: arr[0]
# })
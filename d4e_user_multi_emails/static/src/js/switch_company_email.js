odoo.define('d4e_user_multi_emails.SwitchCompanyEmail', function(require) {
"use strict";

var config = require('web.config');
var core = require('web.core');
var session = require('web.session');
var SystrayMenu = require('web.SystrayMenu');
var Widget = require('web.Widget');
var switchCompany = require('web.SwitchCompanyMenu')

var _t = core._t;

switchCompany.include({


    willStart: function () {
        var self = this;
        this.allowed_company_ids = String(session.user_context.allowed_company_ids)
                                    .split(',')
                                    .map(function (id) {return parseInt(id);});
        this.user_companies = session.user_companies.allowed_companies;
        this.current_company = this.allowed_company_ids[0];
        this.current_company_name = _.find(session.user_companies.allowed_companies, function (company) {
            return company[0] === self.current_company;
        })[1];
        this.current_user_id = this._rpc({
                model: 'res.users',
                method: 'search_read',
                domain: [['id', '=', session.user_context['uid']]],
            }).then(function (user){
                self._rpc({
                    model: 'res.partner',
                    method: 'search_read',
                    domain: [['id', '=', user[0]['partner_id'][0]]],
               }).then(function (partner){
                    self.partner_email = partner[0]['email']
                    var emails = partner[0]['email_by_company']
                    for (var i in emails){
                        var em = self._rpc({
                            model: 'user.emails',
                            method: 'search_read',
                            domain: [['id', '=', emails[i]]],
                            }).then(function (em){
                                var email = em[0]['email']
                                var company = em[0]['company_id']
                                if(self.current_company == company[0]){
                                    self._rpc({
                                            model: 'res.partner',
                                            method: 'write',
                                            args: [[partner[0]['id']], {email: email}],
                                         });
                                    console.log(partner[0]['email'])
                                }
                            });

                    }
                });
            });

        return this._super.apply(this, arguments);

    },

});

});

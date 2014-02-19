define([
    'text!templates/login.html'
    , 'views/alert'

    , '/static/js/parsley.min.js'
], function(
    template
    , AlertView
){
    var View = Backbone.View.extend({
        tpl: _.template(template)
        , render: function(){
            this.$el.html(this.tpl());
            return this;
        }
        , afterRendered: function() {
            this.$('input[type=tel]').focus();
        }
        , events: {
            'click button#loginButton':'onLogin'
        }
        , onLogin: function(e) {
            var me = this;
            var alert = new AlertView();
            alert.clean();
            var afterTag = '#loginButton';

            if (this.$('#login').parsley('validate')) {
                // TODO: parsley should trim whitespaces
                // TODO: use bootstrap validation states and icons
                var inputPassword = this.$('input[type=password]');
                var aid = $.trim(this.$('input[type=tel]').attr('value'));
                var password = $.trim(inputPassword.attr('value'));
                $.post('/api/user/auth', {'aid':aid, 'password': password}).done(function(data){
                    window.user = data;
                    me.router.navigate('dashboard', true);
                }).fail(function(jqXHR, textStatus, errorThrown){
                    if (jqXHR.status==403){
                        alert.show(afterTag, 'Maybe wrong password');
                        inputPassword.attr('value', '');
                        inputPassword.focus();
                    }else{
                        alert.show(afterTag, jqXHR.status + ' ' + errorThrown);
                    }
                });
            }
            e.preventDefault();
        }
    });
    return View;
});

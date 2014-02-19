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
            if (this.$('#login').parsley('validate')) {
                // TODO: parsley should trim whitespaces
                // TODO: use bootstrap validation states and icons
                var aid = $.trim(this.$('input[type=tel]').attr('value'));
                var password = $.trim(this.$('input[type=password]').attr('value'));
                $.post('/api/user/auth', {'aid':aid, 'password': password}).done(function(user){
                    console.log(user)
                }).fail(function(jqXHR, textStatus, errorThrown){
                    if (jqXHR.status==403){
                        console.log('parsley error')
                    }else{
                        var alert = new AlertView();
                        alert.show('#login h2', jqXHR.status + ' ' + errorThrown);
                    }
                });
            }
            e.preventDefault();
        }
    });
    return View;
});

define([
    'text!templates/auth.html'
], function(
    template
){
    var View = Backbone.View.extend({
        tpl: _.template(template)
        , getCurrentUser: function() {
            var me = this;
            $.get('/api/user').done(function(data){
                console.log(data);
            }).fail(function(jqXHR, textStatus, errorThrown){
                if (jqXHR.status==403){
                    me.router.navigate('login', true);
                };
            });
        }
        , render: function(){
            this.$el.html(this.tpl());
            this.getCurrentUser();
            return this;
        }
    });
    return View;
});

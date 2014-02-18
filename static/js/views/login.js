define([
    'text!templates/login.html'
], function(template){
    var View = Backbone.View.extend({
        tpl: _.template(template)
        , render: function(){
            this.$el.html(this.tpl());
            return this;
        }
        , events: {
            'click button':'onLogin'
        }
        , onLogin: function(e) {
            e.preventDefault();
        }
    });
    return View;
});

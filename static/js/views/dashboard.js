define([
    'text!templates/dashboard.html'
], function(template){
    var View = Backbone.View.extend({
        tpl: _.template(template)
        , render: function(){
            this.$el.html(this.tpl({'name':window.user.name}));
            return this;
        }
    });
    return View;
});

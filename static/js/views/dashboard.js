define([
    'text!templates/dashboard.html'
], function(template){
    var View = Backbone.View.extend({
        tpl: _.template(template)
        , render: function(){
        	// FIXME: window user lost after refresh
        	var name = 'Admin';//window.user.name;
            this.$el.html(this.tpl({'name':name}));
            return this;
        }
    });
    return View;
});

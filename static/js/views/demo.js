define([
    'text!templates/demo.html'
], function(template){
    var View = Backbone.View.extend({
        tpl: _.template(template)
        , render: function(){
            this.$el.html(this.tpl());
            return this;
        }
    });
    return View;
});

define([
    'text!templates/alert.html'
], function(template){
    var View = Backbone.View.extend({
        tpl: _.template(template)
        , show: function(afterTag, message){
        	var me = this;
        	this.clean();

        	$(afterTag).after(this.tpl({'message':message}));
        	$('#alert').bind('closed.bs.alert', function(){
        		me.clean();
        	});
        }
        , clean: function() {
        	$('#alert').remove();
        }
    });
    return View;
});

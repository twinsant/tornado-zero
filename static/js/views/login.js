define([
    'text!templates/login.html'
    , '/static/js/parsley.min.js'
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
            if (this.$('#login').parsley('validate')) {
                console.log('valid')
            }
            e.preventDefault();
        }
    });
    return View;
});

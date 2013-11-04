require.config({
    urlArgs: 'bust=1'
});

define([
    'views/demo'
], function(
    DemoView
){
    var AppRouter = Backbone.Router.extend({
        routes: {
            'demo':'demo'
            , '*other':'defaultRoute'
        }
        ,initialize: function(){
        }
        ,demo: function(){
            //ga('send', 'pageview', '/demo');
            this.view = new DemoView();
            this.render();
        }
        ,defaultRoute: function(other){
        }
        , render: function() {
            $('#container').html(this.view.render().el);
            return this;
        }
    });
    
    var router = new AppRouter();
    Backbone.history.start();

    router.navigate('demo', true);
});

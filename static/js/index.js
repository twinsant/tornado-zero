require.config({
    urlArgs: 'bust=1'
});

define([
    'views/demo'
    , 'views/auth'
    , 'views/login'
], function(
    DemoView
    , AuthView
    , LoginView
){
    var AppRouter = Backbone.Router.extend({
        routes: {
            'demo':'demo'
            , 'auth':'auth'
            , 'login':'login'
            , '*other':'defaultRoute'
        }
        ,initialize: function(){
        }
        ,demo: function(){
            //ga('send', 'pageview', '/demo');
            this.view = new DemoView();
            this.render();
        }
        , auth: function() {
            this.view = new AuthView();
            this.view.router = this;
            this.render();
        }
        , login: function() {
            this.view = new LoginView();
            this.view.router = this;
            this.render();
        }
        ,defaultRoute: function(other){
        }
        , render: function() {
            $('#container').html(this.view.render().el);
            if (this.view.afterRendered) {
                this.view.afterRendered();
            }
            return this;
        }
    });
    
    var router = new AppRouter();
    Backbone.history.start();

    router.navigate('demo', true);
});

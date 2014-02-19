var Session = Backbone.Model.extend({
});

var SessionManager = Backbone.Collection.extend({
    model: Session
    , localStorage: new Backbone.LocalStorage('session')
});

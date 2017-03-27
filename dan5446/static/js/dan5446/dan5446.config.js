(function() {
    'use strict';

    angular
        .module('dan5446', [])
        .config(config);

    config.$inject = ['$httpProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */
    function config($httpProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    };

})();
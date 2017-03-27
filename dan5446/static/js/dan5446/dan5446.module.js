/**
 * Created by dmm3685 on 3/27/15.
 */

(function() {
    'use strict';

    angular
        .module('dan5446', ['ng.django.forms'])
        .controller('LogController', LogController);

    LogController.$inject = ['$scope', '$http'];

    function LogController($scope, $http) {
        var LogController = {
            initialize: initialize
        };

        function initialize(recipe, style, date) {

        }
    };

})();
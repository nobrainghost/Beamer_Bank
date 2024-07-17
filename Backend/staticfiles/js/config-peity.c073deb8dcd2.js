/* --------------------------------------------------------------------------
 * File        : config-peity.js
 * Author      : indonez
 * Author URI  : http://www.indonez.com
 *
 * Indonez Copyright 2020 All Rights Reserved.
 * -------------------------------------------------------------------------- */

    'use strict';

    const FinaLineChart = {
        theme_plugin: function() {
            const element = document.querySelectorAll('.fina-line-chart');
            element.forEach(chart => {
                peity(chart, 'line', {
                    delimiter: ',',
                    fill: '#e5f7f1',
                    max: null,
                    min: 40,
                    stroke: '#00b276',
                    strokeWidth: 2,
                    width: '100%',
                    height: '100'
                })
            })
        },
        theme_init: function() {
            FinaLineChart.theme_plugin();
        }
    }
    
    document.addEventListener('DOMContentLoaded', function() {
        FinaLineChart.theme_init();
    });
var app = new Vue({
    el: '#routelist',
    data: {
        routes:
        {
            // 1 : {start: 1, end: 2, events:[1,2]},
            // 2 : {start: 3, end: 4, events:[3,4]},
        },
        events: {
            1 : { start: 1, end: 2, time: '2019-08'},
            2 : { start: 1, end: 2, time: '2019-08'},
            3 : { start: 1, end: 2, time: '2019-08'},
            4 : { start: 1, end: 2, time: '2019-08'},
        },
        cities: {
            1: {name: 'Amsterdam'},
            2: {name: 'Berlin'},
            3: {name: 'Paris'},
            4: {name: 'Tokyo'},
        },
    },
    delimiters: ['[[',']]']
})

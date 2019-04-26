
var app = new Vue({
    el: '#routeplaner',
    components: {
        vuejsDatepicker
    },
    data: {
        routes: null,
        events: null,
        cities: null,
        start_id_selected: null,
        start_id_error: false,
        end_id_selected: null,
        end_id_error: false,
        time_selected: null,
        time_error: false,
        route_id_selected: null,
        route_id_error: false
    },
    methods: {
        newRoute: function(event){
            axios.post('/route')
            .then(response => {

                axios.get('/route')
                .then(response => {
                    this.routes = response.data;
                });
            })
        },
        removeRoute: function (route) {
            axios.delete('/route/' + route.id)
            .then(response => {

                axios.get('/route')
                .then(response => {
                    this.routes = response.data;
                });
            })
        },
        newEvent: function(route){

        },
        customFormatter(date) {
            return moment(date).format('YYYY-MM-DD');
        },
        eventModalClose: function(){
            // this.start_id_selected = null;
            // this.end_id_selected = null;
            // this.time_selected = null;
            // this.route_id_selected = null;

            // this.start_id_error = false;
            // this.end_id_error = false;
            // this.time_error = false;
            // this.route_id_error = false;
        },
        addEvent: function(route_id){
            this.route_id_selected = route_id;
        },
        createEvent: function(){
            let self = this;
            axios.post('/event', {
                'time' : this.time_selected,
                'start_id': this.start_id_selected,
                'end_id': this.end_id_selected,
                'route_id': this.route_id_selected,
            })
            .then(function (response) {

              console.log(response);
            })
            .catch(function (error) {

              if (error.response){
                if ('start_id' in error.response.data.error){

                    self.start_id_error = error.response.data.error.start_id;
                }
                if ('end_id' in error.response.data.error){
                    self.end_id_error = error.response.data.error.end_id;
                }
                if ('time' in error.response.data.error){
                    self.time_error = error.response.data.error.time;
                }
                if ('route_id' in error.response.data.error){
                    self.route_id_error = error.response.data.error.route_id;
                }
             }
            });
        }

    },
    mounted () {
        //let self = this;
        axios.get('/city')
        .then(response => {
            this.cities = response.data;
        })

        axios.get('/event')
        .then(response => {
            this.events = response.data;
        })
        axios.get('/route')
        .then(response => {
            this.routes = response.data;
        });




        //$(this.$refs.eventModal).on("hidden.bs.modal", this.eventModalClose)

    },
    delimiters: ['[[',']]'],
})

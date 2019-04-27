
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
        route_id_error: false,
        modal_status: 'create',
        event_id_selected: null
    },
    methods: {
        loadData: function(api=['route', 'event', 'city']){

            let self = this;

            if(api.indexOf('city') > -1){
                axios.get('/city')
                .then(response => {
                    self.cities = response.data;
                })
            }

            if(api.indexOf('event') > -1){
                axios.get('/event')
                .then(response => {
                    self.events = response.data;
                })
            }

            if(api.indexOf('route') > -1){
                axios.get('/route')
                .then(response => {
                    self.routes = response.data;
                });
            }
        },
        newRoute: function(event){
            axios.post('/route')
            .then(response => {
                this.loadData();
            })
        },
        removeRoute: function (route) {
            let self = this;
            axios.delete('/route/' + route.id)
            .then(response => {

                Vue.delete(self.routes, route.id);
            })
        },
        removeEvent: function (event_id){

            let self = this;
            axios.delete('/event/' + event_id)
            .then(response => {
                Vue.delete(self.events, event_id);
            })
        },
        customFormatter(date) {
            return moment(date).format('YYYY-MM-DD');
        },
        eventModalClose: function(){
            this.start_id_selected = null;
            this.end_id_selected = null;
            this.time_selected = null;
            this.route_id_selected = null;

            this.start_id_error = false;
            this.end_id_error = false;
            this.time_error = false;
            this.route_id_error = false;
        },
        addEvent: function(route_id){
            this.route_id_selected = route_id;
            this.modal_status = 'create';
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

                self.loadData();
                $('#eventModal').modal("hide");
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
        },
        editEvent: function(event){

            this.modal_status = 'edit';

            this.start_id_selected = event.start_id;
            this.end_id_selected = event.end_id;
            this.time_selected = event.time;

            this.event_id_selected = event.id;
        },
        updateEvent: function(event){

            let self = this;

            axios.put('/event/' + self.event_id_selected, {
                'time' : self.time_selected,
                'start_id': self.start_id_selected,
                'end_id': self.end_id_selected,
                'route_id': 0
            })
            .then(function (response) {

                self.loadData(['event']);
                $('#eventModal').modal("hide");
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

            })
        }

    },
    mounted () {

        this.loadData();

        $(this.$refs.eventModal).on("hidden.bs.modal", this.eventModalClose)

    },
    delimiters: ['[[',']]'],
})

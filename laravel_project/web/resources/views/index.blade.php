@extends('base')


@section('content')
<div id="routeplaner">
    <div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
        <h1 class="display-4">Route Planer Laravel</h1>
        <p class="lead">Each route contains multiple events</p>
        <button type="button" class="btn btn-xs btn-outline-success" v-on:click="newRoute">New Route</button>
    </div>

    <div  class="container" v-cloak>
            <div class="card-deck mb-3 text-center" v-for="route in routes" v-if="routes">
                <div class="card mb-4 box-shadow" >
                        <div class="card-header d-flex flex-column flex-md-row align-items-center">
                                <h4 class="my-0 mr-md-auto font-weight-normal">Route [[route.id]]</h4>
                                <button type="button" class="btn btn-xs btn-outline-danger" v-on:click="removeRoute(route)">Remove</button>

                        </div>
                        <div class="card-body" >
                                <h3 class="card-title pricing-card-title"></h3>

                                <p class="card-text"  >
                                    <ul class="list-group">
                                        <li class="list-group-item d-flex row align-items-center" v-for="event_id in route.events" v-if="cities && events[event_id]">
                                            <span class="col text-left">
                                                    [[ cities[events[event_id].start_id].name ]]
                                                    to
                                                    [[ cities[events[event_id].end_id].name ]]

                                            </span>
                                            <span class="col text-left">
                                                [[ events[event_id].time ]]

                                            </span>

                                            <button type="button" class="btn btn-xs btn-outline-success mr-1"
                                                data-toggle="modal" data-target="#eventModal"
                                                v-on:click="editEvent(events[event_id])"
                                            >Edit</button>
                                            <button type="button" class="btn btn-xs btn-outline-danger" v-on:click="removeEvent(event_id)">Remove</button>
                                        </li>
                                    </ul>

                                </p>

                                <div class="card-text">
                                    <button type="button" class="btn btn-xs btn-block btn-outline-success"
                                            data-toggle="modal" data-target="#eventModal"
                                            v-on:click="addEvent(route.id)"
                                            >Add Event</button>
                                </div>

                        </div>
                </div>
            </div>

    </div>


    <div ref="eventModal"  class="modal fade" id="eventModal" tabindex="-1" role="dialog" aria-labelledby="eventModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">

                  <h5 class="modal-title" id="eventModalLabel" v-if="modal_status=='create'">New Event in Route [[route_id_selected]]</h5>
                  <h5 class="modal-title" id="eventModalLabel" v-else>Edit Event</h5>

                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body">
                  <form class="needs-validation" was-validated>
                    <div class="form-group">

                        <label for="start-id-input" class="col-form-label">Start</label>
                        <select required class="form-control" v-model="start_id_selected" id="start-id-input" v-on:change="()=>{start_id_error=null}">
                            <option v-bind:value="city.id" id="start_id" v-for="city in cities">[[ city.name ]]</option>
                        </select>
                        <div class="invalid-feedback d-block" v-if="start_id_error">[[start_id_error]]</div>

                    </div>
                    <div class="form-group">
                        <label for="end-id-input" class="col-form-label">End</label>
                        <select required class="form-control" v-model="end_id_selected" id="end-id-input" v-on:change="()=>{end_id_error=null}">
                            <option v-bind:value="city.id" id="end_id" v-for="city in cities">[[ city.name ]]</option>
                        </select>
                        <div class="invalid-feedback d-block" v-if="end_id_error">[[end_id_error]]</div>
                    </div>
                    <div class="form-group">
                        <label for="time-input" class="col-form-label">Date</label>
                        <vuejs-datepicker required
                            placeholder="Select Date" v-model="time_selected" id="time-input"
                            :format="customFormatter"  v-on:closed="()=>{time_error=null}">
                        </vuejs-datepicker>
                        <div class="invalid-feedback d-block" v-if="time_error">[[time_error]]</div>
                    </div>

                  </form>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>

                  <button type="button" class="btn btn-primary" v-on:click="createEvent" v-if="modal_status=='create'">Create</button>
                  <button type="button" class="btn btn-primary" v-on:click="updateEvent" v-else>Save</button>

                </div>
              </div>
            </div>
          </div>

</div>

@stop

@section('end_script')
<script src="{{ asset('js/moment.js') }}"></script>
<script src="{{ asset('js/vuejs-datepicker.min.js') }}"></script>
<script src="{{ asset('js/axios.min.js') }}"></script>

<script>
  axios.defaults.xsrfHeaderName = "X-CSRFToken";
  axios.defaults.xsrfCookieName = 'XSRF-TOKEN';
</script>
<script src="{{ asset('js/demo.js') }}"></script>
@stop

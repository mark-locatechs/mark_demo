<?php

namespace App\Http\Controllers\Api;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;

class EventController extends ApiController
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $resp = $this->client->get(config('app.api_base_url').'event');

        return json_decode($resp->getBody(), true);
    }


    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $resp = $this->client->post(config('app.api_base_url').'event', ['json' => $request->json()->all()]);

        return json_decode($resp->getBody(), true);
    }


    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        $resp = $this->client->put(config('app.api_base_url')."event/{$id}", ['json' => $request->json()->all()]);

        return json_decode($resp->getBody(), true);
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        $resp = $this->client->delete(config('app.api_base_url')."event/{$id}");

        return json_decode($resp->getBody(), true);
    }
}

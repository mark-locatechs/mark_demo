<?php

namespace App\Http\Controllers\Api;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;

class ApiController extends Controller
{
    protected $client;

    public function __construct(){

        $this->client = new \GuzzleHttp\Client();
    }
}

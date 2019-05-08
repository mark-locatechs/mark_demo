<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('index');
})->name('index');

Route::get('/lorem', function () {
    return view('index');
})->name('lorem');

Route::resource('api/city', 'Api\CityController');
Route::resource('api/route', 'Api\RouteController');
Route::resource('api/event', 'Api\EventController');

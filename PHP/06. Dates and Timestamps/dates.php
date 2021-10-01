<?php
    /*
    echo date('d/'); //Day
    echo date('m/'); //Month
    echo date('Y'); //Year 
    echo date('l'); //Day of the week
    echo date('Y-m-d');
    */

    /*
    echo date('h '); //Hour
    echo date('i '); //Minutes
    echo date('s '); //Seconds
    echo date('a '); //Am of PM
    */

    // Set time zone
    /*
    date_default_timezone_set('America/Recife');
    echo date('h:i:sa');
    */

    $timestamp = mktime(12, 30, 00, 12, 15, 2001); // number of seconds of this date

    //echo $timestamp;

    //echo date('m/d/Y h:i:sa', $timestamp);

    $timestamp2 = strtotime('7:00pm March 22 2016');
    $timestamp3 = strtotime('tomorrow');
    $timestamp4 = strtotime('next Sunday');
    $timestamp5 = strtotime('+2 Months');
    $timestamp6 = strtotime('+2 Days');

    //echo $timestamp2;

    echo date('d/m/Y h:i:sa', $timestamp3);
?>
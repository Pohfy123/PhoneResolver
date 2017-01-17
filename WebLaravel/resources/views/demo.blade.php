@extends('masterpage')

@section('title')Demo
@endsection

@section('css-js')
    <link href="css/demo.css" rel="stylesheet">
@endsection

@section('content')
    <div class="content content-demo-input">
        <div class="searchForm">
            <h3><b>Input</b></h3>
            <div class="form-group">
                <input type="text" class="form-control" placeholder="Enter url, keyword, text ...">
            </div>
            <div class="center">
                <button type="button" class="btn btn-primary">Analyze</button>
            </div>
        </div>
    </div>
@endsection
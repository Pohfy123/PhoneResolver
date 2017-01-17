@extends('masterpage')

@section('title')Result
@endsection

@section('css-js')
    <link href="css/result.css" rel="stylesheet">
@endsection

@section('content')
    <div class="content content-demo-input">
        <div class="container container-all row">
            <div class="col-md-4 container-left">
                <h3><b>Input</b> <span class="tag label label-warning input-tag">URL</span></h3>
                <textarea class="input-textarea form-control" rows="1" id="text"></textarea>
                <br>
                <button type="button" class="btn btn-primary">Analyze</button>
            </div>
            <div class="col-md-8 container-right">
                <div class="btn-group">
                    <button type="button" class="btn btn-primary active"><span class="fui-eye"></span> Result</button>
                    <button type="button" class="btn btn-primary"><span class="fui-arrow-left"></span><span class="fui-arrow-right"></span> JSON</button>
                </div>
            </div>
        </div>
    </div>

    <script src="js/result.js"></script>
@endsection

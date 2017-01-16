@extends('masterpage')

@section('title')Result
@endsection

@section('css-js')
    <link href="css/result.css" rel="stylesheet">
@endsection

@section('content')
    <div class="container container-all">
        <div class="container-left">
            <h3><b>Input</b> <span class="tag label label-warning input-tag">URL</span></h3>
            <textarea class="input-textarea form-control" rows="1"></textarea>
        </div>
        <div class="container-right">
            <div class="btn-group">
                <button type="button" class="btn btn-primary active"><span class="fui-eye"></span> Result</button>
                <button type="button" class="btn btn-primary"><span class="fui-arrow-left"></span><span class="fui-arrow-right"></span> JSON</button>
            </div>
        </div>
    </div>

    <script>
        $("textarea").resizable();
        $('textarea').autoResize();
    </script>
@endsection

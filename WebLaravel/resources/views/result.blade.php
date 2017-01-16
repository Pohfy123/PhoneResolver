@extends('masterpage')

@section('title')Result
@endsection

@section('css-js')
    <link href="css/result.css" rel="stylesheet">
@endsection

@section('content')
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
                <br>
                <br>
                <br>
            </div>
            <table class="table table-bordered">
                <thead>
                <tr>
                    <th>#</th>
                    <th>Category</th>
                    <th>Score</th>
                    <th>Confident ?</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <th scope="row">1</th>
                    <td>Food</td>
                    <td>0.5342132</td>
                    <td>Yes</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Restaurant</td>
                    <td>0.2323132</td>
                    <td>No</td>
                </tr>
                </tbody>
            </table>

        </div>
    </div>

    <script src="js/result.js"></script>
@endsection

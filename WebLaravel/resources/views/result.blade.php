@extends('masterpage')

@section('title')Result
@endsection

@section('css-js')
    <link href="css/result.css" rel="stylesheet">
    <script src="js/result.js"></script>
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
                    <button type="button" class="btn btn-primary active" id="btn-result"><span class="fui-eye"></span> Result</button>
                    <button type="button" class="btn btn-primary" id="btn-json"><span class="fui-arrow-left"></span><span class="fui-arrow-right"></span> JSON</button>
                </div>
                <br>
                <br>
                <table class="table table-bordered table-result">
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
                <pre class="json hide">
                    {
                        "request": {
                          "input": "http://wongnai.com",
                          "type": "url",
                          "api": "analyze",
                          "version": "1.0.0",
                          "resolvedPageUrl": "https://www.wongnai.com/"
                        },
                        "language": "th",
                        "result": {
                            "keywords": [
                                  "ร้านอาหาร",
                                  "ร้านซูชิ",
                                  "กรุงเทพมหานคร"
                            ],
                            "contents": "ร้านอาหารแนะนำ ดูทั้งหมด  Recommended by JOHNNIE WALKER"
                        },
                        "category": {
                            "d1": {
                              "confidence": 0.49049994349479675,
                              "value": "restaurant"
                            },
                            "d2": {
                              "confidence": 0.31968462467193604,
                              "value": "seafood restaurant"
                            }
                        }
                    }
                </pre>
            </div>
        </div>
    </div>
@endsection

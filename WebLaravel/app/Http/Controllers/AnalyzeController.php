<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class AnalyzeController extends Controller
{
    public function index()
    {
        return response()->json([
        'name' => 'Abigail',
        'state' => 'CA'
        ]);
    }
    private function isURL($str) {
        return preg_match('|^http(s)?://[a-z0-9-]+(.[a-z0-9-]+)*(:[0-9]+)?(/.*)?$|i', $str);
    }
    private function isPhone($str) {
        return preg_match('/^\+?([0-9]{1,4})\)?[-. ]?([0-9\-]){6,}[0-9]$/', $str);
    }

    /**
     * @param Request $request
     * @return array|mixed
     */
    public function webCategorize(Request $request){
        $MIN_LEN_TEXT = 50;
        $input_val = $request->input('input_value');
        if( empty($input_val) )
            return array(
                'status'=> '400',
                'msg'=> 'No input.'
            );

        if($this->isURL($input_val))
            $input_type = 'url';
        else if( $this->isPhone($input_val) )
            $input_type = 'phone';
        else if( strlen($input_val) < $MIN_LEN_TEXT )
            $input_type = 'keyword';
        else
            $input_type = 'text';

        // This is the data you want to pass to Python
        $data = array(
            'input'=> array(
                'type' => $input_type,
                'value' => $input_val,
            )
        );

        set_time_limit (200);
        $postdata = http_build_query($data);
        $opts = array('http' =>
            array(
                'method'  => 'POST',
                'header'  => 'Content-type: application/x-www-form-urlencoded',
                'content' => $postdata
            )
        );
        curl_setopt($opts, CURLOPT_FOLLOWLOCATION, true);
        $context  = stream_context_create($opts);
        $result = file_get_contents('http://localhost:5000/phone', false, $context);


//
//        // Execute the python script with the JSON data
//        $result = shell_exec('python ./analytic/single_keyword_classification.py > log' . base64_encode(json_encode($data)));
//
//        // Decode the result
//        $resultData = json_decode($result, true);
//
//        // This will contain: array('status' => 'Yes!')
//        $output = array(
//            "request" => array(
//                "input" => $input_val,
//                "type" => $input_type,
//                "api" => "analyze",
//                "version" => "1.0.0"
//            ),
//            "language" => "th",
//            "result" => $resultData['data']
////            "result" => array(
////                "keywords" => array(
////                    "ร้านอาหาร",
////                    "ร้านซูชิ",
////                    "กรุงเทพมหานคร"
////                ),
////                "contents" => "ร้านอาหารแนะนำ ดูทั้งหมด  Recommended by JOHNNIE WALKER",
////                "category" => array(
////                    "d1" => array(
////                        "confidence"=> 0.49049994349479675,
////                        "value"=> "restaurant"
////                    ),
////                    "d2" => array(
////                        "confidence"=> 0.31968462467193604,
////                        "value"=> "seafood restaurant"
////                    )
////                )
////            )
//        );
        return $result;
    }
}

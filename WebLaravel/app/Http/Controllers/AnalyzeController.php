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
        $input_type = strtolower($request->input('input_type'));
        if( empty($input_val) )
            return array(
                'status'=> '400',
                'msg'=> 'No input.'
            );
//
////        read from file
////        $file = fopen("alldata.csv","r");
//        $csv = array_map('str_getcsv', file('alldata.csv'));
//        array_walk($csv, function(&$a) use ($csv) {
//            $a = array_combine($csv[0], $a);
//        });
//        foreach($csv as $data){
//            return typeOf($data);
//            list($value,$req) = explode(",", $data,2);
////            if($value == $input_val){
////                return $req;
////            }
//            return $value;
//            return $csv[0];
//        }
//        return $csv;

//        $csv = array_map('str_getcsv', file('alldata.csv'));
//        while($row=fgets($file)){
//            // can parse further $row by usingstr_getcsv
//            list($value,$req) = explode(",", $row,2);
//            if($value == $input_val){
//                return $req;
//          }
//        }
//        fclose($file);

//        end read from file


//
//        if($this->isURL($input_val))
//            $input_type = 'url';
//        else if( $this->isPhone($input_val) )
//            $input_type = 'phone';
//        else if( strlen($input_val) < $MIN_LEN_TEXT )
//            $input_type = 'keyword';
//        else
//            $input_type = 'text';


        // This is the data you want to pass to Python
        $data = array(
            'input'=> array(
                'type' => $input_type,
                'value' => $input_val,
            )
        );

        $url = "";
        if($input_type == "phone"){
            $url = 'http://localhost:5000/phone';
        }else if($input_type == "url"){
            $url = 'http://localhost:5000/url';
        }else if($input_type == "keyword"){
            $url = 'http://localhost:5000/keyword';
        }else{
            $url = 'http://localhost:5000/text';
        }
        $data_json = json_encode($data);
        set_time_limit (200);
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS,$data_json);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        $result  = curl_exec($ch);
        curl_close($ch);


//        $list = array (
//            array($input_val,$result),
//        );
//        $fp = fopen('alldata.csv', 'a');
//        foreach ($list as $fields) {
//            fputcsv($fp, $fields);
//        }
//        fclose($fp);


        return $result;
    }
}

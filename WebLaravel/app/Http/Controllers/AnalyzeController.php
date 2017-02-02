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

        // Execute the python script with the JSON data
        $result = shell_exec('python testWeb.py ' . base64_encode(json_encode($data)));

        // Decode the result
        $resultData = json_decode($result, true);

        // This will contain: array('status' => 'Yes!')
        return $resultData;
    }
}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Obtener datos de una API desde PHP</title>
</head>
<body>
    <?php 
    try {
        
        $ch = curl_init();
        $url = 'https://pokeapi.co/api/v2/pokemon/ditto';
    
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    
        $response = curl_exec($ch);
        if (curl_errno($ch)) {
            $error_msg = curl_error($ch);
            echo'<h1>'. "Error: " . $error_msg. '</h1>';
        }
        else {
            curl_close($ch);
            $data = json_decode($response, true);
            echo '<h1>'. $data['name']. '</h1>';
        }
        var_dump($data);
    } catch (\Throwable $th) {
        echo '<h1>'. $th->getMessage(). '</h1>';
    }
    ?>
</body>
</html>
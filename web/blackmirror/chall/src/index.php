<?php
// flag is in another: FLAG_
include "config.php";

if (isset($_GET["view-source"])) {
    highlight_file(__FILE__);
}

function mirrorify($query) {
	$s_query = str_replace(["--", "#"], "?", $query);
    $trans = [
        "(" => ")", ")" => "(",
        "<" => ">", ">" => "<",
        "[" => "]", "]" => "[",
        "{" => "}", "}" => "{",
    ];
	$m_query = strtr($s_query, $trans);
	return $s_query . strrev($m_query);
}

function unmirrorify($text) {
    $plain = substr($text, 0, strlen($text)/2);
    return  $plain;
}

$db = dbconnect();
if (isset($_GET["query"]) && is_string($_GET["query"])) {
    $mirrorified = mirrorify($_GET["query"]);
    $sql = "SELECT * FROM series WHERE name LIKE (\"%${mirrorified}%\")";
    $result = mysqli_query($db, $sql);
    $episodes = mysqli_fetch_all($result);
} else {
    $result = mysqli_query($db, "SELECT * FROM series");
    $episodes = mysqli_fetch_all($result);
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Black Mirror Episodes</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Rubik+Glitch&display=swap');

    /* General Styles */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background-color: #131314;
      color: #b6b6b6;
      font-family: Arial, sans-serif;
    }

    .title {
      font-family: "Rubik Glitch", system-ui;
      font-weight: 400;
      font-size: 3em;
      text-align: center;
      margin: 20px 0;
    }

    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px;
    }

    /* Input Field */
    .search-input {
      width: 70%;
      padding: 10px;
      background-color: #222;
      color: #fff;
      border: 1px solid #444;
      font-size: 1em;
      border-radius: 5px;
      outline: none;
    }

    .search-input:focus {
      border-color: #b6b6b6;
    }

    table {
      width: 100%;
      max-width: 1200px;
      border-collapse: collapse;
      margin: 20px 0;
      color: #b6b6b6;
    }

    th,
    td {
      padding: 12px;
      text-align: left;
      border: 1px solid #444;
    }

    th {
      background-color: #333;
      color: #fff;
    }

    tr:nth-child(even) {
      background-color: #222;
    }

    tr:hover {
      background-color: #444;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
      .title {
        font-size: 2em;
      }

      table {
        width: 100%;
        overflow-x: auto;
      }

      th,
      td {
        padding: 8px;
        font-size: 0.9em;
      }

      .search-input {
        width: 80%;
      }
    }

    @media (max-width: 480px) {
      .title {
        font-size: 1.5em;
      }

      th,
      td {
        padding: 6px;
        font-size: 0.8em;
      }

      .search-input {
        width: 90%;
      }
    }

    .query {
      width: 80%;
      display: flex;
      align-content: center;
      justify-content: space-evenly;
      margin-bottom: 20px;
    }

    .btn {
      width: 20%;
      background-color: #b6b6b6;
      border: 1px solid #444;
      font-size: 1em;
      color: #444;
      border-radius: 5px;
    }

    .ep-title {
      color: #b6b6b6
    }
  </style>
</head>

<body>

  <div class="container">

    <h2 class="title">BLACK MIRROR</h2>

    <div class="query">
      <input type="text" id="search" class="search-input" placeholder="Search for episodes...">
      <button class="btn" id="query">Query</button>
    </div>

    <table id="episodesTable">
      <tr>
        <th>Episode Name</th>
        <th>Season</th>
        <th>Episode Number</th>
      </tr>
      <?php foreach ($episodes as $ep) { ?>
      <tr>
        <td>
          <a class="ep-title" href="<?= $ep[3]; ?>"><?= unmirrorify($ep[0]); ?></a>
        </td>
        <td><?= $ep[1]; ?></td>
        <td><?= $ep[2]; ?></td>
      </tr>
      <?php } ?>
    </table>
  </div>
  <script>
    query.addEventListener("click", (event) => {
      window.location = `?query=${encodeURIComponent(search.value)}`
    })
    
    window.addEventListener("keydown", (event) => {
      if (event.key == "Enter") {
        window.location = `?query=${encodeURIComponent(search.value)}`
      }
    })
  </script>

</body>

<!-- ?view-source -->

</html>
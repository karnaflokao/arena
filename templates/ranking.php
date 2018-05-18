<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
	<style>
	a{color: #000;}
table {
    border-collapse: collapse;
    background: #ccc;
    width: 60%;
   	margin: 0 auto;
   	margin-top: 50px;
}
.confro{background: #FF4500;}
td, th {
    border: 1px solid #dddddd;
    text-align: center;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
body{
	 background: url("img/dra.jpg")no-repeat ;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
}

</style>
</head>
<body>
<div class="btn-group btn-group-justified" role="group" aria-label="..." style="margin-top: 100px;">
  <div class="btn-group" role="group">
  </div>
  <div class="btn-group" role="group">
  </div>
  <div class="btn-group" role="group">
  </div>
  <div class="btn-group" role="group" style="text-align: center;">
  	<button type="button" class="btn btn-success"><a style="text-decoration: none;" href="/confronto/"><span class="glyphicon glyphicon-arrow-left"></span>Confrontos</a></button>
  </div>
  <div class="btn-group" role="group">
  	
  </div>
</div>


<div class="btn-group btn-group-justified" role="group" aria-label="...">
  <div class="btn-group" role="group">
  {% se latest_dbz_list%}
   <table>
	<tr class="confro">
		<th>RANKING</th>
		<th>GUERREIROS Z</th>
		<th>PARTIDAS</th>
		<th>PONTOS</th>
		<th>TITULO</th>
		<th>TEMPORADA</th>
	</tr>	
	{% de dbz em latest_dbz_list%}
	<tr>
		<td>{{dbz.posicao}} </td>
		<td><a href="/dbx/perfil/ {{dbz.id}}/">{{dbz.guerreiro}}</a></td>
		<td>{{dbz.partidas}}</td>
		<td>{{dbz.pontos}}</td>
		<td>{{dbz.titulo}}</td>
		<td>{{dbz.season}}</td>
	</tr>
	{% endfor%}
</table>
  </div>
</div>
{% outro %}
	< p > Sem jogadores para calcular o rank. </ p >
{% fim se %}
</body>
</html>

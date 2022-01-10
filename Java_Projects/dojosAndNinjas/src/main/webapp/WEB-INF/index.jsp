<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
	rel="stylesheet">
<link rel="stylesheet" href="css/style.css" />
<meta charset="UTF-8">
<title>Dojos and Ninjas</title>
</head>
<body>
	<div class="container" id="wrapper">
		<div class="container" id="dojo-table">
			<table class="table table-hover">
				<thead>
					<tr>
						<th>Name</th>
						<th>Location</th>
					</tr>
				</thead>
				<tbody>
				<c:forEach items="${ dojos }" var="dojo">
					<tr>
						<td><a href="/dojos/${dojo.id}">${ dojo.name }</a></td>
						<td>${ dojo.location }</td>
					</tr>
				</c:forEach>
				</tbody>
			</table>
		</div>
		<div class="container" id="bottom">
			<a class="btn btn-lg btn-primary" href="/dojos/new">Add Dojo</a>
					<a href="/ninjas/new" class="btn btn-lg btn-dark">Add Ninja</a>
		<a href="/" class="btn btn-lg btn-outline-secondary">All Dojos</a>
		<a href="/ninjas" class="btn btn-lg btn-outline-dark">All Ninjas</a>
		</div>
	</div>
</body>
</html>
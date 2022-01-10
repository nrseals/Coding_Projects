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
<title>All Ninjas</title>
</head>
<body>
	<div class="container" id="wrapper">
		<div class="container" id="ninja-table">
			<h1>Look at all these Ninjas!</h1>
			<table class="table table-hover">
				<thead>
					<tr>
						<th>First Name</th>
						<th>Last Name</th>
						<th>Age</th>
						<th>Dojo</th>
					</tr>
				</thead>
				<tbody>
				<c:forEach items="${ ninja }" var="n">
					<tr>
						<td>${ n.firstName }</td>
						<td>${ n.lastName }</td>
						<td>${ n.age }</td>
						<td><a href="/dojos/${n.dojo.id}">${ n.dojo.name }</a></td>
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
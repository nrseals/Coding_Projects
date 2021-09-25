<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html>
<html>
<head>
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
	rel="stylesheet">
<link rel="stylesheet" href="css/style.css" />
<meta charset="UTF-8">
<title>Add new Dojo</title>
</head>
<body>
	<div class="container" id="wrapper">
		<div class="container" id="dojo-form">
			<form:form action="/" method="POST" modelAttribute="dojo">
				<div class="form-group">
					<form:label path="name">Dojo Name</form:label>
		        	<form:errors path="name"/>
		        	<form:input class="form-control" path="name"/>
	        	 </div>
	        	 <div class="form-group">
					<form:label path="location">Dojo Location</form:label>
		        	<form:errors path="location"/>
		        	<form:input class="form-control" path="location"/>
	        	 </div>
	        	 <input type="submit" class="btn btn-lg btn-outline-success" value="Submit">
			</form:form>
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
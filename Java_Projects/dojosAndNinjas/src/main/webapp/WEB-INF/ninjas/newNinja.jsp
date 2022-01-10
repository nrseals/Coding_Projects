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
<title>Add a Nina</title>
</head>
<body>
	<div class="contaier" id="wrapper">
			<div class="container" id="ninja-form">
			<form:form action="/ninjas" method="POST" modelAttribute="ninja">
				<div class="form-group">
		        <form:label path="dojo">Dojo Name</form:label>
		        <form:errors path="dojo"/>
		        <form:select class="form-control" path="dojo">
		        <c:forEach items="${ dojo }" var="dojo">
		        	<option value="${ dojo.id }">${ dojo.name }</option>
		        </c:forEach>
		        </form:select>
		    </div>
				<div class="form-group">
					<form:label path="firstName">First Name:</form:label>
		        	<form:errors path="firstName"/>
		        	<form:input class="form-control" path="firstName"/>
	        	 </div>
	        	 <div class="form-group">
					<form:label path="lastName">Last Name:</form:label>
		        	<form:errors path="lastName"/>
		        	<form:input class="form-control" path="lastName"/>
	        	 </div>
	        	 <div class="form-group">
					<form:label path="age">Age:</form:label>
		        	<form:errors path="age"/>
		        	<form:input class="form-control" path="age"/>
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
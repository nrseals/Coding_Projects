<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%> 
<!DOCTYPE html>
<html>
	<head>
		<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
			rel="stylesheet">
		<meta charset="UTF-8">
	<title>Great Ideas</title>
</head>
	<body>
		<div class="container" id="wrapper">
			<div class="row">
			<div class="col-6" id="left">
				<form:form class="user-form" action="/" method="post" modelAttribute="registration">
					<h2>Register</h2>
				 	<div class="form-group">
				        <form:label path="name">Name</form:label>
				        <form:errors path="name"/>
				        <form:input class="form-control" path="name"/>
				    </div>
				    <div class="form-group">
				        <form:label path="email">Email</form:label>
				        <form:errors path="email"/>
				        <form:input type="email" class="form-control" path="email" />
				    </div>
				     <div class="form-group">
				        <form:label path="password">Password</form:label>
				        <form:errors path="password"/>
				        <form:password class="form-control" path="password" />
				    </div>
				    <div class="form-group">
				        <form:label path="passwordConfirmation">Confirm Password</form:label>
				        <form:errors path="passwordConfirmation"/>
				        <form:password class="form-control" path="passwordConfirmation" />
				    </div>
				    <input type="submit" class="btn btn-lg btn-primary" value="Register">
				</form:form>
			</div>
			
			<div class="col-6" id="right">
				<form action="/login" class="user-form" method="post">
					<h2>Login</h2>
					<span>${ error }</span>
					<div class="form-group">
						<label for="email">Email</label>
						<input type="email" name="email" id="email" class="form-control" />
					</div>
					<div class="form-group">
				        <label for="password">Password</label>
				        <input type="password" name="password" id="password" class="form-control" />		        
				    </div>
				    <input type="submit" class="btn btn-lg btn-outline-success" value="Login">
				</form>
			</div>
			</div>
		</div>
	</body>
</html>
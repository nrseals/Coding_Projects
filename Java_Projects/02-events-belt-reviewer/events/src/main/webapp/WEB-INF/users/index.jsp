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
	<title>Events: Belt Review!</title>
</head>
	<body>
		<div class="container" id="wrapper">
			<div class="container" id="top">
				<form:form class="user-form" action="/" method="post" modelAttribute="registration">
					<h2>Register</h2>
				 	<div class="form-group">
				        <form:label path="firstName">First Name</form:label>
				        <form:errors path="firstName"/>
				        <form:input class="form-control" path="firstName" />
				    </div>
				    <div class="form-group">
				        <form:label path="lastName">Last Name</form:label>
				        <form:errors path="lastName"/>
				        <form:input class="form-control" path="lastName" />
				    </div>
				    <div class="form-group">
				        <form:label path="email">Email</form:label>
				        <form:errors path="email"/>
				        <form:input type="email" class="form-control" path="email" />
				    </div>
				    <div class="form-group">
				        <form:label path="city">City</form:label>
				        <form:errors path="city"/>
				        <form:input class="form-control" path="city" />
				    </div>
				    <div class="form-group">
				        <form:label path="state">State</form:label>
				        <form:errors path="state"/>
						<form:input class="form-control" path="state"/>
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
				    <input type="submit" class="btn btn-lg btn-success" value="Register">
				</form:form>
			</div>
			<div class="container" id="wrapper">
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
	</body>
</html>
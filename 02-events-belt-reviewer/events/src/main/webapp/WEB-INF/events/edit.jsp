<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html>
<html>
	<head>
		<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
			rel="stylesheet"/>
		<meta charset="UTF-8">
<title>Events: Belt Reviewer!</title>
</head>
<body>
		<div class="container">
			<h2>Edit <strong>${ event.name }</strong></h2>
			<form:form action="/events/${ event.id }" method="post" modelAttribute="event">
				<input type="hidden" name="_method" value="put">
				<form:hidden value="${ userId }" path="planner"/>
				<div class="form-group">
					<form:label path="name">Name</form:label>
					<form:errors path="name"></form:errors>
					<form:input class="form-control" path="name"></form:input>
				</div>
				<div class="form-group">
					<form:label path="date">Date</form:label>
					<form:errors path="date"></form:errors>
					<form:input class="form-control" type="date" path="date"></form:input>
				</div>
				 <div class="form-group">
			        <form:label path="city">City</form:label>
			        <form:errors path="city"/>
			        <form:input class="form-control" path="city" />
			    </div>
			    <div class="form-group">
			        <form:label path="state">State</form:label>
			        <form:errors path="state"/>
					<form:input class="form-control" path="state"></form:input>
			    </div>
			    <button>Update Event</button>
			</form:form>
		</div>
	</body>
</html>
package com.nathanseals.events.repositores;

import org.springframework.data.repository.CrudRepository;

import com.nathanseals.events.models.User;

public interface UserRepository extends CrudRepository<User, Long> {
	User findByEmail(String email);
}

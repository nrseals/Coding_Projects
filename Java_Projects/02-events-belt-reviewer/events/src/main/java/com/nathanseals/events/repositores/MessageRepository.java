package com.nathanseals.events.repositores;

import org.springframework.data.repository.CrudRepository;

import com.nathanseals.events.models.Message;

public interface MessageRepository extends CrudRepository<Message, Long> {

}

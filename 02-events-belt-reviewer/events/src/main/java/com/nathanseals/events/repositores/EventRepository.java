package com.nathanseals.events.repositores;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.nathanseals.events.models.Event;



@Repository
public interface EventRepository extends CrudRepository<Event, Long>{
	List <Event> findAll();
}

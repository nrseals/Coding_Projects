package com.nathanseals.dojosandninjas.controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.nathanseals.dojosandninjas.models.Dojo;
import com.nathanseals.dojosandninjas.models.Ninja;
import com.nathanseals.dojosandninjas.services.MainService;

@Controller
public class HomeController {
	private final MainService serv;
	public HomeController(MainService serv) {
		this.serv = serv;
	}
	//GET Requests
	@RequestMapping("/")
	public String index(Model model) {
		List<Dojo> allDojos = serv.allDojos();
		model.addAttribute("dojos", allDojos);
		return "index.jsp";
	}
	@RequestMapping("/dojos/new")
	public String newDojo(@ModelAttribute("dojo") Dojo dojo) {
		return "dojos/newDojo.jsp";
	}
//	@RequestMapping("/deleteAll")
//	public String delete() {
//		serv.deleteAll();
//		return "redirect:/";
//	}
	
	@RequestMapping("/dojos/{id}")
	public String showDojo(@PathVariable("id")Long id, Model model) {
		Dojo dojo = serv.findDojo(id);
		List<Ninja> ninja = dojo.getNinjas();
		model.addAttribute("dojo", dojo);
		model.addAttribute("ninja", ninja);
		return "dojos/showDojo.jsp";
	}
	
	@RequestMapping("ninjas/new")
	public String newNinja(@ModelAttribute("ninja") Ninja ninja, Model model) {
		List<Dojo> allDojos = serv.allDojos();
		model.addAttribute("dojo", allDojos);
		return "ninjas/newNinja.jsp";
	}
	@RequestMapping("/ninjas")
	public String allNinjas(Model model) {
		List<Ninja> allNinjas = serv.allNinjas();
		model.addAttribute("ninja", allNinjas);
		return "/ninjas/allNinjas.jsp";
	}
	
	//POST Requests
	@RequestMapping(value="/", method=RequestMethod.POST)
	public String dojo(@Valid @ModelAttribute("dojo") Dojo dojo, BindingResult result) {
		if (result.hasErrors()) {
			return "dojos/newDojo.jsp";
		} else {
			serv.createDojo(dojo);
			return "redirect:/";
		}
	}
	@RequestMapping(value="/ninjas", method=RequestMethod.POST)
	public String ninja(@Valid @ModelAttribute("ninja") Ninja ninja, BindingResult result, Model model) {
		if(result.hasErrors()) {
			List<Dojo> allDojos = serv.allDojos();
			model.addAttribute("dojo", allDojos);
			return "ninjas/newNinja.jsp";
		} else {
			serv.createNinja(ninja);
			return "redirect:/ninjas";
		}
	}
}

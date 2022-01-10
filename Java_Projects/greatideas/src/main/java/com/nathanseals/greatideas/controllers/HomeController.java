package com.nathanseals.greatideas.controllers;

import java.util.List;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.nathanseals.greatideas.models.Idea;
import com.nathanseals.greatideas.models.User;
import com.nathanseals.greatideas.services.IdeaService;
import com.nathanseals.greatideas.services.UserService;
import com.nathanseals.greatideas.validators.UserValidator;

@Controller
public class HomeController {
	@Autowired
	private UserService uServ;
	
	@Autowired
	private IdeaService iServ;
	
	@Autowired
	private UserValidator uValid;
	
	//Login/Registration
	
	@RequestMapping("/")
	public String login(@ModelAttribute("registration") User user, Model model) {
		return "login.jsp";
	}
	@RequestMapping(value="/", method=RequestMethod.POST)
	public String Register(@Valid @ModelAttribute("registration") User user, BindingResult result, HttpSession session) {
		uValid.validate(user, result);
		if(result.hasErrors()) {
			return "login.jsp";
		} else {
		User newUser = this.uServ.registerUser(user);
		session.setAttribute("userId", newUser.getId());
		return "redirect:/ideas";
		}
	}
	@RequestMapping(value="/login", method=RequestMethod.POST)
	public String Login(@Valid @RequestParam("email") String email, @RequestParam("password") String password, HttpSession session, RedirectAttributes redirs) {
		if(this.uServ.authenticateUser(email, password)) {
			User user = this.uServ.findByEmail(email);
			session.setAttribute("userId", user.getId());
			return "redirect:/ideas";
		}
		redirs.addFlashAttribute("error", "Invalid Email/Password");
		return "redirect:/";
	}
	//Session
	public Long userSessionId(HttpSession session) {
		if(session.getAttribute("userId") == null)
			return null;
		return (Long)session.getAttribute("userId");
	}
	//Logout
    @RequestMapping("/logout")
    public String logout(HttpSession session) {
        // invalidate session
    	session.invalidate();
        // redirect to login page
    	return "redirect:/";
    }
    
	//Ideas
	
	@RequestMapping("/ideas")
	public String index(@ModelAttribute("idea") Idea idea, Model model, HttpSession session) {
		Long userId = this.userSessionId(session);
		if(userId == null)
			return "redirect:/";
		
		User user = this.uServ.findUserById(userId);
		List <Idea> allIdeas = iServ.findAllIdeas();
		model.addAttribute("ideas", allIdeas);
		model.addAttribute("user", user);
		return "index.jsp";
	}
	@RequestMapping("/ideas/new")
	public String newIdea(Model model, HttpSession session, @ModelAttribute("idea") Idea idea) {
		if(session.getAttribute("userId") == null) {
			return "redirect:/";	
		}
		else {
			Long userId = (Long)session.getAttribute("userId");
			User user = this.uServ.findUserById(userId);
			model.addAttribute("user", user);
			return "new.jsp";
		}
	}
	@RequestMapping(value="/ideas/create", method = RequestMethod.POST)
	public String createNewIdea(HttpSession session, @Valid @ModelAttribute("idea") Idea idea, BindingResult result, RedirectAttributes redirect) {
		if(session.getAttribute("userId") == null) {
			return "redirect:/";	
		}
		if(result.hasErrors()) {
			return "new.jsp";
		}
		else {
			this.iServ.createOneIdea(idea);
			return "redirect:/ideas";
		}
	}
	//delete idea
	@RequestMapping(value="/ideas/{id}/delete")
	public String deleteOneIdea(HttpSession session, @PathVariable("id") Long id) {
		if(session.getAttribute("userId") == null) {
			return "redirect:/";	
		}
		else {
			this.iServ.deleteOneIdea(id);
			return "redirect:/ideas";
		}
	}
	@RequestMapping("/ideas/{id}")
	public String ideaDetail(HttpSession session, @PathVariable("id") Long id, Model model) {
		if(session.getAttribute("userId") == null) {
			return "redirect:/";	
		}
		else {
			Long userId = (Long)session.getAttribute("userId");
			User user = this.uServ.findUserById(userId);
			model.addAttribute("user", user);
			Idea idea = this.iServ.findOneIdea(id);
			model.addAttribute("idea", idea);
			return "show.jsp";
		}
	}
	@RequestMapping("/ideas/{id}/edit")
	public String editIdeaPage(HttpSession session,@PathVariable("id") Long id, Model model,@ModelAttribute("idea") Idea idea) {
		if(session.getAttribute("userId") == null) {
			return "redirect:/";	
		}

		else {
			Idea ideaToBeEdited = this.iServ.findOneIdea(id);
			model.addAttribute("idea", ideaToBeEdited);
			return "edit.jsp";
			
		}
	}
	@RequestMapping(value="/ideas/{id}/update", method = RequestMethod.POST)
	public String ideaUpdate(@Valid @ModelAttribute("idea") Idea idea, BindingResult result, HttpSession session) {
		if(session.getAttribute("userId") == null) {
			return "redirect:/";
		}
		if(result.hasErrors()) {
			return "edit.jsp";
		}else {
			this.iServ.updateOneIdea(idea);
			return "redirect:/ideas";
		}
	}
}

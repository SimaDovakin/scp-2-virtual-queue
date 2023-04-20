"use strict";

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function getPageSectionsObject() {
	const sectionsNodes = document.querySelectorAll('main.page section[id]');
	let sectionsObject = {};

	sectionsNodes.forEach(item => {
		let key = item.getAttribute('id');

		sectionsObject[key] = item;
	});

	return sectionsObject;
}

function getSidebarMenuItemsObject() {
	const menuItemsNodes = document.querySelectorAll('#leftSideBar .menu-item');
	let menuItemsObject = {};

	menuItemsNodes.forEach(item => {
		let key = item.dataset.sectionId;

		menuItemsObject[key] = item;
	});

	return menuItemsObject;
}

const pageSections = getPageSectionsObject();
const menuItems = getSidebarMenuItemsObject();
const queueFormWrapper = document.getElementById('queueFormWrapper');
const addQueueBtn = document.getElementById('addQueueBtn');
const hideQueueFormBtn = document.getElementById('hideQueueFormBtn');
const addQueueForm = document.getElementById('addQueueForm');
const myQueuesSection = document.getElementById('queues');

function clickSidebarMenuItem(e) {
	const menuItem = e.target.closest('.menu-item');

	if (menuItem) {
		const sectionId = menuItem.dataset.sectionId;

		addSectionHash(sectionId);

		activateItem(sectionId, pageSections);
		activateItem(sectionId, menuItems);
	}
}

async function clickOnQueueAction(e) {
	const actionButton = e.target,
				queueItem = actionButton.parentElement.parentElement;

	if (actionButton.classList.contains('btn-item-delete')) {
		await deleteQueueItem(queueItem.dataset.id);
		queueItem.remove();
	}
}

function activateItem(id, items) {
	Object.keys(items).forEach(item => {
		if (item === id && !items[item].classList.contains('active')) {
			items[item].classList.add('active');
		} else if (item !== id) {
			items[item].classList.remove('active');
		}
	});
}

function showQueueForm() {
	addQueueBtn.classList.remove('show');
	queueFormWrapper.classList.add('show');
}

function hideQueueForm(e) {
	queueFormWrapper.classList.remove('show');
	addQueueBtn.classList.add('show');
}

function addQueueItemHTML(queueHTML) {
	myQueuesSection.querySelector('.item-list').innerHTML += queueHTML;
}

async function deleteQueueItem(queueId) {
	const url = `/delete_queue/${queueId}`;

	const response = await fetch(url, {
		method: 'DELETE',
		credentials: 'same-origin',
		headers: {
			"X-Requested-With": "XMLHttpRequest",
			"X-CSRFToken": getCookie("csrftoken")
		}
	});
}

async function submitAddQueueForm(e) {
	e.preventDefault();

	const formData = new FormData(addQueueForm);
	const endpoint = addQueueForm.getAttribute('action');
	const postData = {
		name: formData.get('name'),
		country: +formData.get('country'),
		region: +formData.get('region'),
		city: +formData.get('city'),
		address: formData.get('address')
	};

	const response = await fetch(endpoint, {
		method: 'POST',
		credentials: 'same-origin',
		headers: {
			"X-Requested-With": "XMLHttpRequest",
			"X-CSRFToken": getCookie("csrftoken")
		},
		body: JSON.stringify(postData)
	});
	const responseData = await response.json();
	addQueueItemHTML(responseData['queue_html']);
}

function addSectionHash(sectionId) {
	document.location.hash = sectionId;
}

function resolveSectionHash() {
	const sectionId = document.location.hash.replace('#', '');

	if (sectionId !== '') {
		if (menuItems.hasOwnProperty(sectionId) && pageSections.hasOwnProperty(sectionId)) {
			activateItem(sectionId, pageSections);
			activateItem(sectionId, menuItems);
		}
	}
}

resolveSectionHash();

document.getElementById('leftSideBar').addEventListener('click', clickSidebarMenuItem);
addQueueBtn.addEventListener('click', showQueueForm);
hideQueueFormBtn.addEventListener('click', hideQueueForm);
addQueueForm.addEventListener('submit', submitAddQueueForm);
pageSections.queues.querySelector('.item-list').addEventListener('click', clickOnQueueAction);

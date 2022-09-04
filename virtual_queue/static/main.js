"use strict";

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

function clickSidebarMenuItem(e) {
	const menuItem = e.target.closest('.menu-item');

	if (menuItem) {
		const sectionId = menuItem.dataset.sectionId;

		Object.keys(pageSections).forEach(item => {
			if (item === sectionId && !pageSections[item].classList.contains('active')) {
				pageSections[item].classList.add('active');
			} else if (item !== sectionId) {
				pageSections[item].classList.remove('active');
			}
		});

		Object.keys(menuItems).forEach(item => {
			if (item === sectionId && !menuItems[item].classList.contains('active')) {
				menuItems[item].classList.add('active');
			} else if (item !== sectionId) {
				menuItems[item].classList.remove('active');
			}
		});
	}
}

document.getElementById('leftSideBar').addEventListener('click', clickSidebarMenuItem);

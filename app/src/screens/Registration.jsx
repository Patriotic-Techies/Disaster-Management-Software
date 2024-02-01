import React, { useLayoutEffect, useState } from "react"
import { Keyboard, KeyboardAvoidingView, SafeAreaView,Text, TouchableWithoutFeedback,View,ScrollView, StatusBar} from "react-native"

import Input from "../common/Input"
import Button from "../common/Button"
import api from "../core/api"
import utils from "../core/utils"

import HomeScreen from "./Home"


function Registration({navigation}){

    const [username,  setUsername]  = useState('')
	const [email, setEmail] = useState('')
	const [phoneno,  setPhoneno]  = useState('')
	const [adhaar_no, setAdhaar_no] = useState('')
	const [address, setAddress] = useState('')
	const [pincode, setPincode] = useState('')
	const [organization_name, setOrganization_name] = useState('')
	const [organization_type, setOrganization_type] = useState('')
	const [organization_address, setOrganization_address] = useState('')
	const [location, setLocation] = useState('')
	const [org_pincode, setOrg_Pincode] = useState('')
	const [team_count, setTeam_count] = useState('')
	

	const [usernameError,  setUsernameError]  = useState('')
	const [emailError, setEmailError] = useState('')
	const [phonenoError,  setPhonenoError]  = useState('')
	const [adhaar_noError, setAdhaar_noError] = useState('')
	const [addressError, setAddressError] = useState('')
	const [pincodeError, setPincodeError] = useState('')
	const [organization_nameError, setOrganization_nameError] = useState('')
	const [organization_typeError, setOrganization_typeError] = useState('')
	const [organization_addressError, setOrganization_addressError] = useState('')
	const [locationError, setLocationError] = useState('')
	const [org_pincodeError, setOrg_PincodeError] = useState('')
	const [team_countError, setTeam_countError] = useState('')

	useLayoutEffect(() => {
		navigation.setOptions({
			headerShown: false
		})
	}, [])
	
	function onRegister() {
		// Check username
		const failUsername = !username || username.length < 5
		if (failUsername) {
			setUsernameError('Username must be >= 5 characters')
		}
		// Check firstName
		const failEmail = !email
		if (failEmail) {
			setEmailError('First Name was not provided')
		}
		// Check last Name
		const failPhoneno = !phoneno
		if (failPhoneno) {
			setPhonenoError('phone number was not provided')
		}
		const failAdhaar_no = !adhaar_no
		if (failAdhaar_no) {
			setAdhaar_noError('Aadhar number was not provided')
		}
		const failAddress = !address
		if (failAddress) {
			setAddressError('Address was not provided')
		}
        const failPincode = !pincode 
		if (failPincode) {
			setPincodeError('pincode was not provided')
		}
		const failOrganization_name = !organization_name
		if (failOrganization_name) {
			setOrganization_nameError('Organization name was not provided')
		}
		const failOrganization_type= !organization_type
		if (failOrganization_type) {
			setOrganization_typeError('Organization type was not provided')
		}
		const failOrganization_address = !organization_address
		if (failOrganization_address) {
			setOrganization_addressError('Organization address was not provided')
		}
		const failLocation = !location
		if (failLocation) {
			setLocationError('location was not provided')
		}
		const failOrg_Pincode= !org_pincode
		if (failOrg_Pincode) {
			setOrg_PincodeError('Organization pincode was not provided')
		}
		const failTeam_count = !team_count
		if (failTeam_count) {
			setTeam_countError('Team count was not provided')
		}
		// Break out of the fucntion if there were any issues
		if (failUsername ||
			failEmail ||
			failPhoneno ||
			failAdhaar_no ||
			failAddress||
			failPincode||
			failOrganization_name||
			failOrganization_type||
			failOrganization_address||
			failLocation||
			failOrg_Pincode||
			failTeam_count
			) {
			return
		}
		navigation.navigate('HomeScreen')
		api({
			method: 'POST',
			url: '/chat/register/',
			data: {
				username: username,
				email: email,
				phoneno: phoneno,
				adhaar_no: adhaar_no,
				address: address,
				pincode: pincode,
				organization_name: organization_name,
				organization_type: organization_type,
				organization_address: organization_address,
				location: location,
				org_pincode: org_pincode,
				team_count: team_count,
			}
		})
		.then(response => {
			utils.log('Register', response.data)
		})
		.catch(error => {
			if (error.response) {
				console.log(error.response.data);
				console.log(error.response.status);
				console.log(error.response.headers);
			} else if (error.request) {
				console.log(error.request);
			} else {
				console.log('Error', error.message);
			}
			console.log(error.config);
		})





	}
		


    return (
		
		<SafeAreaView style={{ flex: 1 }}>
			<KeyboardAvoidingView behavior="height" style={{ flex: 1 }}>
			<ScrollView style={ {flex: 1}}>
				<TouchableWithoutFeedback onPress={Keyboard.dismiss}>
					<View style={{ flex: 1, justifyContent: 'center', paddingHorizontal: 16 }}>

						<Text 
							style={{ 
								textAlign: 'center', 
								marginBottom: 24, 
								fontSize: 36, 
								fontWeight: 'bold' 
							}}
						>
							Register
						</Text>

						<Input 
							title='Name' 
							value={username}
							error={usernameError}
							setValue={setUsername}
							setError={setUsernameError}
						/>


						<Input 
							title='Email'
							value={email}
							error={emailError}
							setValue={setEmail}
							setError={setEmailError}
						/>
						
						<Input 
							title='phone number'
							value={phoneno}
							error={phonenoError}
							setValue={setPhoneno}
							setError={setPhonenoError}
						/>

						<Input 
							title='Aadhar number'
							value={adhaar_no}
							error={adhaar_noError}
							setValue={setAdhaar_no}
							setError={setAdhaar_noError}
						/>
						<Input 
							title='Address'
							value={address}
							error={addressError}
							setValue={setAddress}
							setError={setAddressError}
						/>
						<Input 
							title='pincode'
							value={pincode}
							error={pincodeError}
							setValue={setPincode}
							setError={setPincodeError}
						/>
						<Input 
							title='Organization Name'
							value={organization_name}
							error={organization_nameError}
							setValue={setOrganization_name}
							setError={setOrganization_nameError}
						/>
						<Input 
							title='Organization Type'
							value={organization_type}
							error={organization_typeError}
							setValue={setOrganization_type}
							setError={setOrganization_typeError}
						/>
						<Input 
							title='Organization Address'
							value={organization_address}
							error={organization_addressError}
							setValue={setOrganization_address}
							setError={setOrganization_addressError}
						/>
						<Input 
							title='Organization location'
							value={location}
							error={locationError}
							setValue={setLocation}
							setError={setLocationError}
						/>
						<Input 
							title='Organization Pincode'
							value={org_pincode}
							error={org_pincodeError}
							setValue={setOrg_Pincode}
							setError={setOrg_PincodeError}
						/>
						<Input 
							title='Team Count'
							value={team_count}
							error={team_countError}
							setValue={setTeam_count}
							setError={setTeam_countError}
						/>

                    <Button title='Register' onPress={() => { onRegister }} />

					</View>
				</TouchableWithoutFeedback>
				</ScrollView>
			</KeyboardAvoidingView>
			</SafeAreaView>
			
		
	)

}

export default Registration
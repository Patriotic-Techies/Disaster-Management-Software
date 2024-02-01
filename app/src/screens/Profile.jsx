import { FontAwesomeIcon } from "@fortawesome/react-native-fontawesome"
import React from "react"
import { SafeAreaView,Text,View,Image, TouchableOpacity, StyleSheet, ScrollView } from "react-native"
import useGlobal from "../core/global"
import { launchCamera,launchImageLibrary } from "react-native-image-picker"
import utils from "../core/utils"
import api from "../core/api"
import Thumbnail from "../common/Thumbnail"




function ProfileImage() {
	const uploadThumbnail = useGlobal(state => state.uploadThumbnail)
	const user = useGlobal(state => state.user)

	return (
		<TouchableOpacity 
		style={{ marginBottom: 10 }}
			onPress={() => {
				launchImageLibrary({includeBase64:true}, (response) => {
					//utils.log('launchImageLibrary', response)
					if (response.didCancel) return
					const file = response.assets[0]
					uploadThumbnail(file)
				})
			}}>
			<Thumbnail
			url={user.thumbnail}
			size={170}
			alignItems='center'
			justifyContent= 'center'
			position= 'absolute'
			left={60}
			width={40}
			height={20}
			
			/>
		
			
			<View
				style={{
					position: 'left',
					bottom: 25,
					left: 120,
					backgroundColor: '#202020',
					width: 40,
					height: 40,
					borderRadius: 10,
					alignItems: 'center',
					justifyContent: 'center',
					borderWidth: 5,
					borderColor: 'white'
				}}
			>
				<FontAwesomeIcon
					icon='pencil'
					size={10}
					alignItems='center'
					justifyContent='center'
					color='#d0d0d0'
					
					
				/>
			</View>
		</TouchableOpacity>
	)
}

function ProfileLogout(){

    const logout=useGlobal(state=>state.logout)

    return (
		<TouchableOpacity
			onPress={logout}
			style={{
				flexDirection: 'row',
				height: 52,
				borderRadius: 26,
				alignItems: 'center',
				justifyContent: 'center',
				paddingHorizontal: 26,
				backgroundColor: '#202020',
				marginTop: 30,
				bottom:80
			}}
		>
			<FontAwesomeIcon
				icon='right-from-bracket'
				size={20}
				alignItems='center'
				color='#d0d0d0'
				style={{ marginRight: 12}}
			/>
			<Text
				style={{
					fontWeight: 'bold',
					color: '#d0d0d0'
				}}
			>
				Logout
			</Text>
		</TouchableOpacity>
	)
}

function ProfileEdit(){
	const user=useGlobal(state=>state.user)
	return (
		<TouchableOpacity
		
			style={{
				flexDirection: 'row',
				height: 52,
				borderRadius: 26,
				alignItems: 'center',
				justifyContent: 'center',
				paddingHorizontal: 6,
				backgroundColor: '#202020',
				marginTop: 30,
				bottom:80
			}}
		>
			<FontAwesomeIcon
				icon='right-from-bracket'
				size={5}
				alignItems='right'
				color='#d0d0d0'
				style={{ marginRight: 5}}
				position= 'right'
				bottom= {20}
				left= {120}
				backgroundColor= '#202020'
				borderRadius= {5}
				justifyContent= 'center'
				borderWidth= {5}
				borderColor= 'white'
			/>
			<Text
				style={{
					fontWeight: 'bold',
					color: '#d0d0d0'
				}}
			>
				Edit
			</Text>
		</TouchableOpacity>
	)

}



function ProfileScreen(){
	const user=useGlobal(state=>state.user)
    return(
        <View style={{
            flex:1,
            alignItems:'left',
            paddingTop:0,
        }}>
            <ProfileImage/>
            <Text
             style={{
                textAlign: 'center',
				color: '#303030',
				fontSize: 20,
				fontWeight: 'bold',
				bottom:20,
				left:90,
			    top:-160
             }}
            >
              {user.name}
            </Text>
            <Text
             style={{
             textAlign: 'center',
             color: '#606060',
             fontSize: 20,
			 bottom:25,
			 left:90,
			 top:-150
            }}
            >
                @{user.username}
            </Text>
			<ProfileEdit/>
			<Text style={styles.profileInfo}>Email: {user.email}</Text>
			<Text style={styles.profileInfo}>Phone Number: {user.phone_no}</Text>
			<Text style={styles.profileInfo}>Aadhar Number: {user.adhaar_no}</Text>
			<Text style={styles.profileInfo}>Address: {user.address}</Text>
			<Text style={styles.profileInfo}>Location: {user.location}</Text>
			<Text style={styles.profileInfo}>Pincode: {user.pincode}</Text>
			<Text style={styles.profileInfo}>Organization Name: {user.organization_name}</Text>
			<Text style={styles.profileInfo}>Organization Type: {user.organization_type}</Text>
			<Text style={styles.profileInfo}>Organization Address: {user.organization_address}</Text>
			<Text style={styles.profileInfo}>Organization Pincode: {user.Org_pincode}</Text>
			
            <ProfileLogout/>
        </View>
    )

}
const styles = StyleSheet.create({
    profileInfo: {
		fontWeight: 'bold',
        textAlign: 'left',
        color: '#303030',
        fontSize: 14,
        marginTop: 20,
		bottom:10,
		left:20,
		top:-60
    }
})


export default ProfileScreen
// Leetcode
// https://leetcode.com/problems/design-parking-system/

package leetcode

// ParkingSystem ...
type ParkingSystem struct {
	spaces []int
}

// Constructor ...
func Constructor(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{
		spaces: []int{big, medium, small},
	}
}

// AddCar ...
func (instance *ParkingSystem) AddCar(carType int) bool {
	instance.spaces[carType-1]--
	return instance.spaces[carType-1] >= 0
}
